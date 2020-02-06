var arr=[1,3,4,13,5,6,2,7,8,9];



var prime=function(){
    for(var i=0;i<arr.length+1;i++)
    {
        if(arr[i]==2)
           {
               document.write(arr[i]+' ');
           }
       for(var j=2;j<arr[i];j++)     
       {
           
           if (arr[i]%j===0){
               break;
           }
           else{
            document.write(arr[i]+' ');
            break;
           }
           
           }
          
    }
    
}
prime();