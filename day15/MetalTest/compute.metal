#include <metal_stdlib>
#include "MetalTest-Bridging-Header.h"
using namespace metal;


kernel void beacon_sensor(constant MyData *data [[ buffer(0) ]],
                          constant int *data_size   [[ buffer(1) ]],
                          device   float *resultArray [[ buffer(2) ]],
                                   uint2   index [[ thread_position_in_grid ]]) {
    int target_row = index[0];
    int target_col = index[1];
    bool hash = false;
    
    for (int i = 0; i < data_size[0]; i++) {
        int sensor_col = data[i].sensor_col;
        int sensor_row = data[i].sensor_row;
        int beacon_col = data[i].beacon_col;
        int beacon_row = data[i].beacon_row;
        
        int dist_to_beacon = abs(beacon_col - sensor_col) + abs(beacon_row - sensor_row);
        int dist_to_target = abs(target_col - sensor_col) + abs(target_row - sensor_row);
        if (dist_to_target <= dist_to_beacon) {
            hash = true;
            break;
        }
    }
    if (hash == false) {
        resultArray[0] = float(target_col);
        resultArray[1] = float(target_row);
    }
}
