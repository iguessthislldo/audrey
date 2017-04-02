var api = new RestClient('http://localhost:8000');
api.res('tasks');

$(function(){
    api.tasks.get().then(function(tasks){
        let list = new Task_List_View(Task.from_objects(tasks));
        $('#app').append(list.element);
    });
});
