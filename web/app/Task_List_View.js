class Task_List_View {
    constructor(tasks) {
        this.tasks = tasks;
        this.element = $(`
            <div id="tasks">
                <div style="margin-bottom: 10px;" class="btn-group">
                    <button type="button" class="btn btn-default">
						<i class="fa fa-plus" aria-hidden="true"></i>
                    </button>
                </div>
            </div>
        `);
        tasks.map(task => this.element.append((new Task_View(task)).element));
    }
}

