class Task_View {
    constructor(task) {
        this.task = task;
        this.element = $(`
            <div class="panel panel-default" id="view_${task.id}">
                <div class="panel-body">
                    ${task.name}
                    <input type="checkbox" class="pull-right">
                </div>
            </div>
        `);
        this.element.click(function(e) {
            if($(e.target).is('input')){
                //e.preventDefault();
                return;
            }
            var modal_view = new Task_Modal_View(task);
        }); 
    }
}

