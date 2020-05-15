class ArithmeticTaskRunner {

    constructor() {
        this.tasks = []
        Object.defineProperty(this, 'taskCount', {
            get: function() {
                return this.tasks.length
            }
        });
    }

    addNegationTask() {
        var myNegFunc = (x) => { return -x }
        this.tasks.push(myNegFunc)
    }

    addAdditionTask(y) {
        var myAddFunc = (x) => { return x + y }
        this.tasks.push(myAddFunc)
    }

    addMultiplicationTask(y) {
        var myMultFunc = (x) => { return x * y }
        this.tasks.push(myMultFunc)
    }

    execute(startValue = 0) {
        var temp = startValue;
        for (let i = 0; i < this.tasks.length; i++) {
            temp = this.tasks[i](temp)
        }
        return temp
    }
}

print = console.log

taskRunner = new ArithmeticTaskRunner()
taskRunner.addAdditionTask(2)
taskRunner.taskCount = 5



print(taskRunner.taskCount)