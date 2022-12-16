import MetalKit

func compute() {
    var d1: [[Int32]] = [[2,18,-2,15],[9,16,10,16],[13,2,15,3],[12,14,10,16],[10,20,10,16],[14,17,10,16],[8,7,2,10],[2,0,2,10],[0,11,2,10],[20,14,25,17],[17,20,21,22],[16,7,15,3],[14,3,15,3],[20,1,15,3]]

    let num_rows_cols: Int = 20
//    let num_rows_cols: Int = 4000000
//
//    let d1: [[Int32]] = [[1259754, 1927417, 1174860, 2000000], [698360, 2921616, 1174860, 2000000], [2800141, 2204995, 3151616, 2593677], [3257632, 2621890, 3336432, 2638865], [3162013, 3094407, 3151616, 2593677], [748228, 577603, 849414, -938539], [3624150, 2952930, 3336432, 2638865], [2961687, 2430611, 3151616, 2593677], [142293, 3387807, 45169, 4226343], [3309479, 1598941, 3336432, 2638865], [1978235, 3427616, 2381454, 3683743], [23389, 1732536, 1174860, 2000000], [1223696, 3954547, 2381454, 3683743], [3827517, 3561118, 4094575, 3915146], [3027894, 3644321, 2381454, 3683743], [3523333, 3939956, 4094575, 3915146], [2661743, 3988507, 2381454, 3683743], [2352285, 2877820, 2381454, 3683743], [3214853, 2572272, 3151616, 2593677], [3956852, 2504216, 3336432, 2638865], [219724, 3957089, 45169, 4226343], [1258233, 2697879, 1174860, 2000000], [3091374, 215069, 4240570, 610698], [3861053, 889064, 4240570, 610698], [2085035, 1733247, 1174860, 2000000]]
    
    var data : [MyData] = []
    for d in d1 {
        let md = MyData(
            sensor_col: d[0],
            sensor_row: d[1],
            beacon_col: d[2],
            beacon_row: d[3]
        )
        data.append(md)
    }
    // Begin the process
    let startTime = CFAbsoluteTimeGetCurrent()
    
    // The GPU we want to use
    let device = MTLCreateSystemDefaultDevice()

    // A fifo queue for sending commands to the gpu
    let commandQueue = device?.makeCommandQueue()

    // A library for getting our metal functions
    let gpuFunctionLibrary = device?.makeDefaultLibrary()

    // Grab our gpu function
    let additionGPUFunction = gpuFunctionLibrary?.makeFunction(name: "beacon_sensor")

    var additionComputePipelineState: MTLComputePipelineState!
    do {
        additionComputePipelineState = try device?.makeComputePipelineState(function: additionGPUFunction!)
    } catch {
      print(error)
    }
    let cnt: [Int32] = [Int32(data.count)]
    
    // Create the buffers to be sent to the gpu from our arrays
    let arr1Buff = device?.makeBuffer(bytes: data,
                                      length: MemoryLayout<MyData>.size * data.count,
                                      options: .storageModeShared)
    let arr2Buff = device?.makeBuffer(bytes: cnt,
                                      length: MemoryLayout<Int32>.size,
                                      options: .storageModeShared)

    let resultBuff = device?.makeBuffer(length: MemoryLayout<Float>.size * 2,
                                        options: .storageModeShared)
    
    // Create a buffer to be sent to the command queue
    let commandBuffer = commandQueue?.makeCommandBuffer()

    // Create an encoder to set vaulues on the compute function
    let commandEncoder = commandBuffer?.makeComputeCommandEncoder()
    commandEncoder?.setComputePipelineState(additionComputePipelineState)

    // Set the parameters of our gpu function
    commandEncoder?.setBuffer(arr1Buff, offset: 0, index: 0)
    commandEncoder?.setBuffer(arr2Buff, offset: 0, index: 1)
    commandEncoder?.setBuffer(resultBuff, offset: 0, index: 2)

    // Figure out how many threads we need to use for our operation
    let threadsPerGrid = MTLSize(width: num_rows_cols + 1, height: num_rows_cols + 1, depth: 1)
    let maxThreadsPerThreadgroup = additionComputePipelineState.maxTotalThreadsPerThreadgroup // 1024
    let threadsPerThreadgroup = MTLSize(width: Int(sqrt(Double(maxThreadsPerThreadgroup))), height: Int(sqrt(Double(maxThreadsPerThreadgroup))), depth: 1)
    commandEncoder?.dispatchThreads(threadsPerGrid,
                                    threadsPerThreadgroup: threadsPerThreadgroup)

    // Tell the encoder that it is done encoding.  Now we can send this off to the gpu.
    commandEncoder?.endEncoding()

    // Push this command to the command queue for processing
    commandBuffer?.commit()

    // Wait until the gpu function completes before working with any of the data
    commandBuffer?.waitUntilCompleted()

    // Get the pointer to the beginning of our data
    var resultBufferPointer = resultBuff?.contents().bindMemory(to: Float.self,
                                                                capacity: MemoryLayout<Float>.size * 2)

    // Print out result array
    let first = Int(resultBufferPointer!.pointee)*4000000
    resultBufferPointer = resultBufferPointer?.advanced(by: 1)
    let sec = Int(resultBufferPointer!.pointee)
    print("\(first + sec)")
    
    // Print out the elapsed time
    let timeElapsed = CFAbsoluteTimeGetCurrent() - startTime
    print("Time elapsed \(String(format: "%.05f", timeElapsed)) seconds")
    print()
}

compute()
