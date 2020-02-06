var a=[]
var n =parseInt(prompt("Enter total no. of numbers to enter"))
for(var j=0;j<n;j++)
{
    a[j]=parseInt(prompt("Enter number to enter array"))
}
var pal=function(){
for(var i=0;i<a.length;i++){
var rem,temp,f=0;
temp=a[i]
while(a[i]>0){
    rem=a[i]%10;
    a[i]=parseInt(a[i]/10);
    f=f*10+rem
}
if (f==temp){
    document.write(temp+"  ")
}
}
}
pal();