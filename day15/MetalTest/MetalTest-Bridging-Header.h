//
//  Common.h
//  MetalTest
//
//  Created by Patrick Cunniff on 12/16/22.
//

#ifndef Common_h
#define Common_h

#ifdef __METAL_VERSION__
#define NS_ENUM(_type, _name) enum _name : _type _name; enum _name : _type
#define NSInteger metal::int32_t
#else
#import <Foundation/Foundation.h>
#endif

#include <simd/simd.h>

typedef struct
{
    int sensor_col;
    int sensor_row;
    int beacon_col;
    int beacon_row;
} MyData ;

#endif /* Common_h */
