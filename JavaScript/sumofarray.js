var arr=[1,2,3,4];
var s=0;
var sum=function(){
    for(var i=0;i<arr.length;i++)
    {
        s=s+arr[i];
    }
    document.write(s)
}
    
sum();