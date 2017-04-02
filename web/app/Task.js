class Task {
    constructor(id, name, description, done) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.done = done;
    }

    static from_objects(objects) {
        return objects.map(o => new Task(o.id, o.name, o.description, o.done));
    }
}

