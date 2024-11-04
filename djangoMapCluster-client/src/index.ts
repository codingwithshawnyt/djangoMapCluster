// Exporting constants used across the application
export {
    ClusterMethod, // Methods for clustering
    GeometryType, // Types of geometries
    IconType, // Types of icons
    SRIDS, // Spatial Reference System Identifiers
    Operators, // Operators for queries
    LogicalOperators, // Logical operators for complex queries
} from "./consts";

// Export classes and types related to map clustering
export { 
    Anycluster, // Main class for map clustering
    Bounds3857, // Bounds using EPSG:3857
    Bounds4326, // Bounds using EPSG:4326
} from "./djangoMapCluster";

// Export types related to map clustering requests and filters
export type {
    Filter, // Type for basic filter
    GetKmeansClusterContentRequestData, // Request data for K-means clustering
    ClusterRequestData, // Generic cluster request data
    MapContentCountRequestData, // Request data for content count
    GroupedMapContentRequestData, // Request data for grouped content
    AreaContentRequestData, // Request data for area content
    FilterList, // List of filters
    NestedFilter, // Nested filter structure
    FilterOrNestedFilter, // Union type for filter or nested filter
    FilterOrNestedFilterList, // List of FilterOrNestedFilter
    Modulations, // Modulations applicable to filters
} from "./djangoMapCluster";

// Export the client class for interacting with the backend
export {
    AnyclusterClient, // Client class for DjangoMapCluster
} from "./djangoMapCluster-client";

// Export settings type for the client
export type {
    AnyclusterClientSettings // Settings for DjangoMapClusterClient
} from "./djangoMapCluster-client";

// Export types related to geometry
export type {
    GeoJSON, // Type for GeoJSON objects
    Marker, // Type for map markers
    Viewport, // Type for the map viewport
} from "./geometry";

// Export types for different clustering responses
export type {
    KmeansCluster, // Type for K-means cluster
    KmeansClusterResponse, // Response type for K-means clustering
    GridCluster, // Type for grid-based clustering
} from "./types";