//Modified from P5 solutions

import Foundation

class RestAPI {
    
    static func getRestaurants() -> [Restaurant] {
        let restaurants = [
            Restaurant(name: "CS 2110", cuisineTypes: [.mexican], credits: [.three], cost: .cheap),
            Restaurant(name: "CS 3110", cuisineTypes: [.japanese], credits: [.four], cost: .cheap),
            Restaurant(name: "CS 4410", cuisineTypes: [.american], credits: [.four], cost: .cheap),
            Restaurant(name: "CS 2800", cuisineTypes: [.italian], credits: [.SU], cost: .expensive)
        ]
        return restaurants
    }
    
    static func getFilters() -> [Filter] {
        var filters: [Filter] = []
        filters.append(contentsOf: Credits.allValues().map({ f in f as Filter }))
//        filters.append(contentsOf: Cost.allValues().map({ f in f as Filter }))
//        filters.append(contentsOf: CuisineType.allValues().map({ f in f as Filter }))
        return filters
    }
}
