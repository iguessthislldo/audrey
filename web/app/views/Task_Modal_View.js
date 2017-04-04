class Task_Modal_View {
    constructor(task) {
        var element = $(`
            <div class="modal fade" id="modal_${task.id}" role="dialog">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title">${task.name}</h4>
                        </div>

                        <div class="modal-body">
                            <textarea class="form-control" rows="3">${task.description}</textarea> 
                        </div>

                        <div class="modal-footer">
                            <a style="margin-top: 10px;" class="btn btn-danger"><i class="fa fa-trash-o fa-lg"></i> Delete</a>
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
        `);
        $('#app').append(element);
        element.modal('toggle');
        element.on('hidden.bs.modal', function (e) {
            element.remove();
        });
        this.element = element;
    }
}

