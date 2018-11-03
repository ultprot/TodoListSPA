<template>
<body>
    <div>
        <div class="jumbotron jumbotron-fluid bg-dark text-white">
            <div class="container">
                <h1>Todo List</h1>
                <p>할 일을 등록해 주세요.</p>    
            </div>
        </div>
                
        <div class="d-flex p-1 flex-row-reverse ">
            <div class="p-2">
                <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#input-content">add+</button>
            </div>
        </div>
        <div class="modal fade" id="input-content">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">새 할 일 추가</h4>
                        <button class="close" type="button" data-dismiss="modal">&times;</button>
                    </div>
                    <div class="modal-body">
                        <form action="#">
                            <div class="form-group">
                                    <label for="subject">제목</label>
                                    <input type="text" class="form-control" v-model="newTodo.subject">
                            </div>
                            <div class="form-group">
                                <label for="content">내용</label>
                                <textarea class="form-control" rows="5" id="content" v-model="newTodo.content"></textarea>
                            </div>
                            <div class="form-group">
                                <div class="btn btn-secondary" data-toggle="collapse" data-target="#newpriority">우선순위 설정</div>
                                <select class="form-control collapse" id="newpriority" v-model="newTodo.priority">
                                    <option selected>우선순위</option>
                                    <option value="1">1</option>                           
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <div class="btn btn-secondary" data-toggle="collapse" data-target="#newexpiration">기한 설정</div>
                                <div id="newexpiration" class="collapse">
                                    <input class="form-control" type="datetime-local" v-model="newTodo.expiration"/>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-secondary" data-toggle="modal" data-target="#input-content" @click="postNewTodo">등록</button>
                        <button class="btn btn-danger" type="button" data-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
        <nav class="navbar bg-dark navbar-dark fixed-bottom"></nav>
    </div>
    
    <ul class="list-group">
        <Todo
            v-for="todo in todos"
            :key="todo.id" 
            :todo="todo"
            @todoDeleted="deleteTodo"
        />
    </ul>

    <div class="d-flex p-1 justify-content-center">
        <img src="../assets/logo.png" class="img-thumbnail">
    </div>
    <nav class="navbar bg-dark navbar-dark fixed-bottom"></nav>
</body>

</template>

<script>
import Todo from './Todo.vue'
export default {
    name: 'Home',
    components:{
        Todo
    },
    data(){
        return {
            todos:
            [
                {
                    id:1,
                    subject:'첫번째 항목입니다. 제목이 매우 길어졌을때 어떻게 되는지 매우 궁금하여 시험해 보려고 합니다.',
                    content:'첫번째 항목의 내용입니다. 잘 나왔으면 좋겠습니다.',
                    priority:5,
                    expiration:'2018-11-30T11:15',
                    done:false
                },
                {
                    id:2,
                    subject:'두번째 항목입니다.',
                    content:'두번째 항목의 내용입니다. 잘 나왔으면 좋겠습니다.',
                    priority:5,
                    expiration:'2018-11-30T11:15',
                    done:false
                },
                {
                    id:3,
                    subject:'세번째 항목입니다.',
                    content:'세번째 항목의 내용입니다. 잘 나왔으면 좋겠습니다.',
                    priority:5,
                    expiration:'2018-11-30T11:15',
                    done:false
                },
                {
                    id:4,
                    subject:'네번째 항목입니다.',
                    content:'네번째 항목의 내용입니다. 잘 나왔으면 좋겠습니다.',
                    priority:5,
                    expiration:'2018-11-30T11:15',
                    done:false
                },
                {
                    id:5,
                    subject:'다섯번째 항목입니다.',
                    content:'다섯번째 항목의 내용입니다. 잘 나왔으면 좋겠습니다.',
                    priority:5,
                    expiration:'2018-11-30T11:15',
                    done:false
                },
                {
                    id:6,
                    subject:'다섯번째 항목입니다.',
                    content:'다섯번째 항목의 내용입니다. 잘 나왔으면 좋겠습니다.',
                    priority:5,
                    expiration:'2018-11-30T11:15',
                    done:false
                },
                {
                    id:8,
                    subject:'다섯번째 항목입니다.',
                    content:'다섯번째 항목의 내용입니다. 잘 나왔으면 좋겠습니다.',
                    priority:5,
                    expiration:'2018-11-30T11:15',
                    done:false
                },
                {
                    id:9,
                    subject:'다섯번째 항목입니다.',
                    content:'다섯번째 항목의 내용입니다. 잘 나왔으면 좋겠습니다.',
                    priority:5,
                    expiration:'2018-11-30T11:15',
                    done:false
                }
            ],
            newTodo:{
                subject:null,
                content:null,
                priority:null,
                expiration:null
            }
        }  
    },
    methods:{
        postNewTodo: function(){
            const baseURI='/item';
            var point=this;
            this.$axios.post(baseURI,{
                subject:this.newTodo.subject,
                content:this.newTodo.content,
                priority:this.newTodo.priority,
                expiration:this.newTodo.expiration
            }).then(function(response){
                var tempTodo=new Object();
                tempTodo.id=response.data.id;
                tempTodo.subject=response.data.subject;
                tempTodo.content=response.data.content;
                tempTodo.priority=response.data.priority;
                tempTodo.expiration=response.data.expiration;
                tempTodo.done=false;
                point.todos.unshift(tempTodo);
                point.newTodo.subject=null;
                point.newTodo.content=null;
                point.newTodo.priority=null;
                point.newTodo.expiration=null;
            }).catch(function(error){
                alert(error);
            })
        },
        deleteTodo: function(currentID){
            var index
            for(index=0;index<this.todos.length;index++)
            {
                if(this.todos[index].id==currentID)
                {
                    break;
                }
            }
            this.todos.splice(index,1);
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
