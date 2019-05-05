//Modified from P5 solutions

import UIKit

protocol Filter {
    var filterTitle: String { get }
}

enum CuisineType: Filter {
    case american
    case mexican
    case italian
    case french
    case japanese
    case chinese
    case greek
    
    var filterTitle: String { //return the enum title with first letter uppercased
        return String(describing: self).localizedUppercase
    }
    
    static func allValues() -> [CuisineType] {
        return [.american,.mexican,.italian,.french,.japanese,.chinese,.greek]
    }
}

enum Credits: Filter {
    case three
    case four
    case SU
    
    var filterTitle: String {
        return String(describing: self).localizedUppercase
    }
    
    static func allValues() -> [Credits] {
        return [.three,.four,.SU]
    }
}

enum Cost: Filter {
    case cheap
    case moderate
    case expensive
    
    var filterTitle: String {
        return String(describing: self).localizedUppercase
    }
    
    static func allValues() -> [Cost] {
        return [.cheap,.moderate,.expensive]
    }
}

class Restaurant: NSObject {
    let name: String
    let cuisineTypes: [CuisineType]
    let credits: [Credits]
    let cost: Cost //only can have one type of cost
    
    init(name: String, cuisineTypes:  [CuisineType], credits: [Credits], cost: Cost) {
        self.name = name
        self.cuisineTypes = cuisineTypes
        self.credits = credits
        self.cost = cost
    }
}
