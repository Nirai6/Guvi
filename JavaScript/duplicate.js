arr=[1,1,1,2,2,2,3,4,5]

var removeDuplicate=function (arr){
    let unique_array = arr.filter(function(elem, index, self) {
        return index == self.indexOf(elem);
    });
    document.write( unique_array);
}



removeDuplicate(arr);