class Task_View {
    constructor(task) {
        let task_element = $(`
            <div id="${task.id}" class="panel panel-default">
            </div>
        `);

        let heading_element = $(`<div class="panel-heading">${task.name}</div>`);

        let checkbox_element = $(`<input type="checkbox" class="pull-right">`);
        checkbox_element.prop("checked", task.done);
        heading_element.append(checkbox_element);

        task_element.append(heading_element);

        this.body_element = $(`
            <div class="panel-body">
                <textarea class="form-control" rows="3">${task.description}</textarea> 
                <a style="margin-top: 10px;" class="btn btn-danger"><i class="fa fa-trash-o fa-lg"></i> Delete</a>
            </div>
        `);
        this.body_element.hide();

        heading_element.click(this.body_element, function(e){
            if($(e.target).is('input')){
                return;
            }
            $(e.data[0]).slideToggle(75);
        });
        task_element.append(this.body_element);

        this.element = task_element;
    }
}

