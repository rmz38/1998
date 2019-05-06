//
//  DisplayRestaurantsCollectionViewFlowLayout.swift
//  Project6solutions
//
//  Created by Natasha Armbrust on 11/6/17.
//  Copyright © 2017 Natasha Armbrust. All rights reserved.
//

import UIKit

class DisplayRestaurantsCollectionViewFlowLayout: UICollectionViewFlowLayout {
    
    let cellWidth: CGFloat = 140
    let cellHeight: CGFloat = 140
    
    override func prepare() {
        super.prepare()
        let edgeInset = (UIScreen.main.bounds.width - 2 * cellWidth) / 3
        itemSize = CGSize(width: cellWidth, height: cellHeight)
        minimumLineSpacing = edgeInset
        minimumInteritemSpacing = edgeInset
        sectionInset = UIEdgeInsets(top: edgeInset, left: edgeInset, bottom: edgeInset, right: edgeInset)
    }
}
