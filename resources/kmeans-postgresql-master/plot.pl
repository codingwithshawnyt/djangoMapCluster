#!/usr/bin/perl --
# Shebang line to specify the interpreter for this script

use strict;  # Enforce some good programming rules
use warnings;  # Enable warnings to help catch common mistakes

use Getopt::Std;  # Use Getopt::Std module for parsing command line options

# Subroutine to check prerequisites for the script
sub check_prereq{
    # Check if gnuplot is installed and in the PATH
    if( !`which gnuplot` ){
        die "gnuplot needs installed in \$PATH$/";  # Exit if gnuplot is not found
    }
    # Check if PostgreSQL client (psql) is installed and in the PATH
    if( !`which psql` ){
        die "psql needs installed in \$PATH$/";  # Exit if psql is not found
    }
}

# Subroutine to display usage information
sub usage{
    print STDERR <<_HELP;
Usage: $0 [-h] [-d dbname] [-k number]
    -h:    print this help
    -d:    database to connect
    -k:    number of class
_HELP
    0;  # Return 0 from the subroutine
}

# Main subroutine that orchestrates other subroutines and logic
sub main{
    &check_prereq();  # Call the check_prereq subroutine
    my %opt;  # Declare a hash to store command line options

    getopts('hd:k:', \%opt);  # Parse command line options

    # If the help option is specified, call the usage subroutine
    if( $opt{'h'} ){
        return &usage;
    }
    # Set the database name, defaulting to "db1" if not specified
    my $dbname = $opt{'d'} || "db1";
    # Set the number of classes, defaulting to 5 if not specified
    my $k = $opt{'k'} || 5;
    # SQL query to perform k-means clustering
    my $sql = <<_SQL;
SELECT kmeans(ARRAY[val1, val2], $k) OVER (), val1, val2
FROM testdata
ORDER BY 1
_SQL
    # Update SQL query to use specific longitude and latitude
    $sql = <<_SQL;
SELECT kmeans(ARRAY[longitude, latitude], 2, array[135.0, 35.0, 139.0, 38.0]) OVER (), longitude, latitude
FROM pref
WHERE latitude IS NOT NULL AND longitude IS NOT NULL
ORDER BY 1
_SQL
    print $sql . $/;  # Print the SQL query
    # Open a filehandle to execute the SQL query using psql
    open my $fh, "-|", qq(psql -A -F ' ' -t -c "$sql" $dbname) or die $!;
    # Open a filehandle to write output to a temporary file
    open my $out, ">", "tmp.dat" or die $!;
    my $prev_k = 0;  # Variable to track the previous cluster number
    # Read the output from the SQL query
    while( <$fh> ){
        chomp;  # Remove newline character
        my( $k, $v1, $v2 ) = split / /, $_;  # Split the line into variables
        # Check if the cluster number has changed
        if( $k != $prev_k ){
            print $out "\n\n";  # Print newlines to separate clusters
            $prev_k = $k;  # Update the previous cluster number
        }
        print $out "$v1 $v2\n";  # Write the data to the temporary file
    }
    close $out;  # Close the output filehandle
    close $fh;  # Close the SQL query filehandle

    my @buf;  # Array to store plot commands
    # Generate plot commands for each cluster
    for my $i ( 0 .. $prev_k ){
        push @buf,  "\"tmp.dat\" index $i:$i using 1:2";
    }
    # Command to plot the data using gnuplot
    my $plotcmd = 'gnuplot -e \'plot ' . join( ", ", @buf ) . '; pause -1\'';
    print $plotcmd . $/;  # Print the plot command
    return `$plotcmd`;  # Execute the plot command
}

# Check if the script is being run directly
if( $0 eq __FILE__ ){
    &main( @ARGV );  # Call the main subroutine with command line arguments
}

