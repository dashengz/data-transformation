# InstaAnalysis
Scrap data from Instagram API and analyze them,
and explain the outcome with simple data visualization.

### Features:
- Get like counts of media containing certain tag,
and create simple charts to visualize the result:
```
e.g.
Like counts of media with #photography over time
^--------------------------------->
^---------------------->
^------------------------>
^---------------->
^------------------->
```
- See if the number of tags added to a post is related
to the number of likes a post received:
```
e.g.
    Num of Tags   |           Num of Likes
<---------------- | --------------------------------->
 <--------------- | ------------------------>
   <------------- | ------------------->
    <------------ | ---------------------->
    <------------ | --------------------->
     <----------- | ---------------->
      <---------- | ------------------------>
      <---------- | --------------------->
      <---------- | -------------------->
       <--------- | ------------------------->
        <-------- | -------------------------->
          <------ | ------------->
            <---- | ------------>
            <---- | -------->
             <--- | ----------------->
             <--- | --------------->
             <--- | ------------>
              <-- | ---------------->
               <- | ----->
                < | ------------>
```
- ...