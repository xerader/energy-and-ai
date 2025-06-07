---
title: Default
tags: 
Ref:
---
# Approach
- There were three waves of new data that was shared. Each wave was analyzed individually and at the end they were combined for more thorough observations

## Initial Data
The initial data included 
- Demographic
- Token Usage
- GPU power usage
related information

### Token Usage
<p align="center">
  <img src="attachments/Pasted%20image%2020250606221032.png" width="400">
</p>
The above figure shows hotspots for specific hours of the day where token usage is noticeably higher. There does not appear to be significant trends when relating on a day to day or month to month basis. 

### Affiliation
<p align="center">
  <img src="attachments/Pasted%20image%2020250606221158.png" width="400">
</p>
Faculty and Affiliates tend to use the most tokens. These are averaged numbers for each demographic. 

<p align="center">
  <img src="attachments/Pasted%20image%2020250606221247.png" width="400">
</p>
There does not seem to be a strong relation between the input and output tokens when relating to the departments. It may be more useful to look at whether specific models are favored by specific departments, which may have specific behaviors for the size of the response tokens

<p align="center">
  <img src="attachments/Pasted%20image%2020250606221447.png" width="400">
</p>
Biomedical research and '22 are the two departments which have the largest average token usage. The top 20 are shown in the above graph. 

### Model Usage

<p align="center">
  <img src="attachments/Pasted%20image%2020250607001352.png" width="400">
</p>

<p align="center">
  <img src="attachments/Pasted%20image%2020250607001620.png" width="400">
</p>


### Power Usage
For this analysis, only the average token usage for the local models was used and compared to the GPU power usage. This can be observed below: 
<p align="center">
  <img src="attachments/Pasted%20image%2020250606221633.png" width="400">
</p>
Hour of day was used to due limited data related to GPU power for the initial data. However, this is an approximation. The token usage data and the GPU power data were not collected during the same time frame. Hence this is not a 1-to-1 comparison. Under the assumption that local model usage has a pattern that is observed above, the graph can be interpreted. 

There was a subset of the second provided data which which could be related. This is as follows: 
<p align="center">
  <img src="attachments/Pasted%20image%2020250606233620.png" width="400">
</p>



#### Combining all the datasets
All of the data was then condensed and plotted at 1 hour intervals. However, this is difficult to observe. So let's look at it at day level intervals instead. 
<p align="center">
  <img src="attachments/Pasted%20image%2020250606235114.png" width="400">
</p>

However even the day level interval is not very interpretable. 
<p align="center">
  <img src="attachments/Pasted%20image%2020250607001112.png" width="400">
</p>


### Next steps
1. See if output length can be predicted from the input length for a given model. If input length too long then maybe set it to be a different model. Requires research on whether it is appropriate. 
