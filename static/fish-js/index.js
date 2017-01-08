/**
 * Created by binbin.zou on 2017/1/4.
 */


$('#add').click(function (){
    var value = $("#time").val();

    if (!value){
        return 0;
    }

    var list = $("#list");
    if (list.children().length >= 10){
        alert('当前提醒数已达到最大值.');
        return 0;
    }

    list.append('<li class="item">' + value+ '<button class="remove" type="button"> x </button></li>');

});


$('.remove').click(function (){
    alert('asx');
});
