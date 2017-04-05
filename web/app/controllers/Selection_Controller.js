class Selection_Controller {
    constructor() {
        this.set = [];
        this.selection = [];
        this.select_mode = false;
    }
    
    add(instance, element) {
        var value = {
            instance: instance,
            element: element,
            index: this.set.length,
            selected: false,
            owner: this
        }
        element.data('owner', value);
        this.set.push(value);
    }

    bind() {
        for (var i = 0; i < this.set.length; i++) {
            this.set[i].element.click(function() {
                var owner = $(this).data('owner');
                var selcon = owner.owner;
                if (owner.owner.select_mode) {
                    owner.selected = !owner.selected;
                    if (owner.selected) {
                        $(this).addClass('selected');
                        selcon.selection.push(owner);
                    } else {
                        $(this).removeClass('selected');
                        selcon.selection.slice(selcon.selection.indexOf(owner), 1);
                    }
                }
            });
        }
    }

    clear() {
        this.selection = [];
        for (var i = 0; i < this.set.length; i++) {
            this.set[i].element.removeClass('selected');
        }
    }

    remove() {
        var copy = this.set.slice(0);
        var item;
        for (var i = 0; i < this.selection.length; i++) {
            item = this.selection[i];
            copy[item.index].element.remove();
            this.set.slice(item.index, 1);
        }
        this.selection = [];
        this.set = copy;
    }
}
