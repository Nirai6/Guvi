var obj = {name : "RajiniKanth", age : 33, hasPets : true};
var s = JSON.stringify(obj)


function printAllKeys(obj){
var o = JSON.parse(s)

 var obj1=[]
for (x in o){
   obj1.push(x);
   
}
console.log(obj1)
}
printAllKeys();



