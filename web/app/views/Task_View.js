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
        this.element.data('owner', this);

        this.element.click({owner: this}, this.normal_function); 
    }

    normal_function(e) {
        var input = $(e.target).is('input')
        if (!$(this).data('owner').owner.select_mode) {
            if (input) {
                return;
            }
            var modal_view = new Task_Modal_View(e.data.owner.task);
        } else {
            if (input) {
                e.preventDefault();
                return;
            }
        }
    }

    selector() {
        return "#view_${this.task.id}";
    }
}

