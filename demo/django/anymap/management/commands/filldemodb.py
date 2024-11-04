'''
    This script populates the database with randomly generated points.
    It operates slowly and does not utilize optimized SQL queries, so it's best to run it in the background.
'''

# Import necessary Django and Python modules
from django.core.management.base import BaseCommand, CommandError
from djangoMapCluster.models import Gardens, GARDEN_STYLES as GardenStyles  # Updated import to reflect new module name and alias
from django.utils import timezone
from django.contrib.gis.geos import GEOSGeometry
import datetime, random

class Command(BaseCommand):
    # Method to add command-line arguments
    def add_arguments(self, parser):
        parser.add_argument('total_markers', type=int)  # Renamed argument for clarity

    # Main handler method for the command
    def handle(self, *args, **options):
        numMarkers = options['total_markers']  # Renamed variable for clarity
        print(f"Creating demo with {numMarkers} markers")  # Updated to use f-string for better readability

        # Loop to create each marker
        for i in range(numMarkers):
            if i % 1000 == 0:
                print(f"{numMarkers - i} markers remaining")  # Updated print statement for clarity

            # Generate random latitude and longitude
            latitude = random.uniform(-84, 84)
            longitude = random.uniform(-179, 179)
            coordinates = GEOSGeometry(f'POINT({longitude} {latitude})', srid=4326)  # Use f-string for coordinate creation
            coordinates.transform(3857)  # Transform coordinates to the web mercator projection

            # Randomly generate other garden attributes
            gardenRating = random.randint(1, 5)  # Renamed variable for clarity
            isFreeEntrance = bool(random.randint(0, 1))  # Renamed variable and converted to boolean
            gardenName = f"Garden {i}"  # Use f-string for name creation

            # Create and save the garden instance
            gardenInstance = Gardens(
                coordinates=coordinates,
                rating=gardenRating,
                name=gardenName,
                free_entrance=isFreeEntrance,
                last_renewal=generate_random_date(),  # Renamed function for clarity
                style=random.choice(GardenStyles)[0]  # Use the alias for garden styles
            )
            gardenInstance.save()

        print("Done. Remember to index your geometric column with a gist index - and to use btree_gist!")

# Function to generate a random date
def generate_random_date():
    """
    Generates a random datetime between two datetime objects.
    """
    current_time = timezone.now()  # Renamed variable for clarity
    start_time = datetime.datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p').replace(tzinfo=datetime.timezone.utc)  # Renamed variable for clarity
    time_difference = current_time - start_time  # Renamed variable for clarity
    seconds_difference = (time_difference.days * 24 * 60 * 60) + time_difference.seconds  # Renamed variable for clarity
    random_seconds = random.randrange(seconds_difference)  # Renamed variable for clarity
    return start_time + datetime.timedelta(seconds=random_seconds)  # Calculate and return the random date