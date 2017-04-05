class Task_List_View {
    constructor(tasks) {
        window.the_task_list_view = this;

        this.element = $(`
            <div id="tasks">
            </div>
        `);

        this.tasks = tasks;
        this.selection = new Selection_Controller();

        var buttons_element = $(`
            <div style="margin-bottom: 10px;" class="btn-group">
            </div>
        `);

        var new_btn_elm= $(`
            <button type="button" class="new_button btn btn-default">
                <i class="fa fa-plus" aria-hidden="true"></i>
                New
            </button>
        `);
        buttons_element.append(new_btn_elm);

        var selection_btns;
        var select_element = $(`
            <button type="button" class="select_button btn btn-default">
                Select
            </button>
        `);
        select_element.data('owner', this);
        select_element.click(function(){
            var o = $(this).data('owner');
            var s = o.selection;
            s.select_mode = !s.select_mode;
            if (s.select_mode) {
                $(this).addClass('activated');
                selection_btns.show();
            } else {
                $(this).removeClass('activated');
                selection_btns.hide();
                s.clear();
            }
        });
        buttons_element.append(select_element);

        this.element.append(buttons_element);

        selection_btns = $(`
            <div style="margin-left: 10px; margin-bottom: 10px;" class="btn-group">
            </div>
        `);

        // Clear Selection
        var clear_selction = $(`
            <button type="button" class="btn btn-default">
                Clear Selection
            </button>
        `);
        clear_selction.data('selection', this.selection);
        clear_selction.click(function(){
            $(this).data('selection').clear();
        });
        selection_btns.append(clear_selction);

        // Delete Selection
        var delete_selction_btn = $(`
            <button type="button" class="btn btn-default">
                Delete Selection
            </button>
        `);

        delete_selction_btn.data('selection', this.selection);
        delete_selction_btn.click(function(e){
            $(this).data('selection').remove();
        });
        selection_btns.append(delete_selction_btn);

        selection_btns.hide();

        this.element.append(selection_btns);

        var view;
        for (var i = 0; i < tasks.length; i++) {
            view = new Task_View(tasks[i]);
            this.selection.add(view, view.element);
            this.element.append(view.element);
        }
        this.selection.bind();
    }
}

