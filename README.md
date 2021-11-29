# 3d-Plant-Dataset-for-Point-Cloud-Reconstruction
(Zhuocheng Guo, Mingwei Sui, Yipeng Liu, Yide Ma)



Milestone:

First stage ( 20/10/2021 - 09/11/2021)

Objectives
• Data augmentation of 3D plant (control randomness of plant and reproduce a large dataset)
• Convert all obj files to point cloud and get them ready for point cloud Neural Network • Select the best fit model, build the model and train it with our dataset. 
• Modify the model based on the analysis of test result
• Test our model with point cloud scan of real plants

We finished two task, 1 have 4 groups of plants generated by vlab, re-implement PFNet work on our end.
The following result is the result we using PFNet and one type of plants, running under 150 epoch, 3000 point cloud models, with 8 hours.  RTX3080
![IMB_FvmUOI](https://user-images.githubusercontent.com/66981525/141042330-556fb669-dcf9-45cd-89a5-91a4db5b4352.gif)

Second stage (09/11/2021 - 06/12/2021)

Task:
1. Re-implement PCN
2. Single-view reconstruction 
