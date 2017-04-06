class Task_View {
    constructor(task) {
        this.task = task;
        this.element = $(`
            <div class="panel panel-default" id="view_${task.id}"> <div class="panel-heading">
                    ${task.name}
                </div>
            </div>
        `);

        this.element.data('owner', this);
        var heading = this.element.find('.panel-heading');

        if (task.tags.length) {
            var body = $(`
                <div class="panel-body">
                    <ul class="inline_tags">
                    </ul>
                </div>
            `);

            var tags_element = body.find('.inline_tags');

            task.tags.forEach(item => {
                console.log(item);
                var s;
                if (typeof(item) === "string") {
                    s = item;
                } else {
                    s = "";
                    for (var prop in item) {
                        s += prop + ":";
                        for (var subindex = 0; subindex < item[prop].length; subindex++){
                            s += " " + item[prop][subindex];
                        }
                    }
                }
                tags_element.append(`
                    <li><a href="">${s}</a></li>
                `);
            });
            
            this.element.append(body);
        }

        heading.click({owner: this}, this.normal_function); 

        var checkbox = $(`
            <div class="checkbox pull-right">
            <svg width="100%" height="100%" viewBox="0 0 58 58">
            <rect
                x="4" y="4" width="50" height="50"
                rx="15" ry="15"
                stroke-width="5"
                fill="none"
            />
            <polyline class="checkmark"
                points="8.6,30.5 24.8,42.5 46.4,12.5"
                stroke-width="7"
                stroke-linecap="butt"
                fill="none"
            />
            </svg>
            </div>
        `);
        var checkmark = checkbox.find('.checkmark');
        if (!task.done) {
            checkmark.addClass('unchecked');
            checkmark.hide();
        }
        heading.append(checkbox);
    }

    normal_function(e) {
        var input = $(e.target).parents('.checkbox').length;
        //var owner = $(this).data('owner');
        var owner = e.data.owner;
        console.log($(this));
        if (!owner.owner.select_mode) {
            if (input) {
                var checkmark = owner.element.find('.checkmark');
                if (checkmark.hasClass('unchecked')) {
                    checkmark.show();
                    checkmark.addClass('checked')
                    checkmark.removeClass('unchecked');
                } else {
                    checkmark.removeClass('checked');
                    checkmark.fadeOut(function(){
                        checkmark.addClass('unchecked')
                    });
                }
                return;
            }
            var modal_view = new Task_Modal_View(e.data.owner.task);
        }
    }

    selector() {
        return "#view_${this.task.id}";
    }
}

