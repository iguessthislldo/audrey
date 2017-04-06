class Task {
    constructor(id, name, description, done, tags) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.done = done;
        this.tags = tags;
    }

    static from_objects(objects) {
        return objects.map(o => new Task(o.id, o.name, o.description, o.done, o.tags));
    }
}

