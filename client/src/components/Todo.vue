<template>
<!--반복-->
<li class="list-group-item">
    <div class="container-fluid">
        <div class="row">
            <div class="col-12 col-sm-9">
                <div class="row">
                    <div class="col-sm-1 col-1">
                        <!--버튼 if-->
                        <div v-on:click="toggleDonity" v-if="todo.done" class="btn btn-secondary" >  </div>
                        <div v-on:click="toggleDonity" v-else class="btn btn-primary" >  </div>
                    </div>
                    <div class="col-sm-11 col-11">
                        <div>
                            <div v-if="todo.done" class="text-muted">{{todo.subject}}</div>
                            <div v-else class="text-dark">{{todo.subject}}</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12  col-sm-3">
                <div class="row">
                    <div class="col-1 offset-7 col-sm-4 offset-sm-0">
                        <div class="dropdown">
                            <button class="btn btn-sm btn-primary dropdown-toggle" type="button" data-toggle="dropdown">
                                +
                            </button>
                            <div class="dropdown-menu ">
                                <div class="dropdown-divider"></div>
                                <div class="dropdown-item" data-toggle="collapse" v-bind:data-target="'#input-content-'+todo.id">수정</div>
                                <div class="dropdown-item" @click="deleteTodo"><div class="text-warning" @click="deleteTodo">삭제</div></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-2 offset-1 col-sm-8 offset-sm-0">
                        <div class="btn btn-sm btn-secondary" data-toggle="collapse" v-bind:data-target="'#content-'+todo.id">내용보기</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="collapse" v-bind:id="'content-'+todo.id">
        <div class="d-flex p-1"></div>
        <div>{{todo.content}}</div>
        <div>우선순위 {{todo.priority}}</div>
        <div>기한 {{todo.expiration}}</div>
    </div>
    <Input @todoChanged="updateTodo" :todo="todo"/>
</li>
</template>

<script>
import Input from './Input.vue'

export default {
    name: 'Todo',
    components:{
        Input
    },
    props:{
        todo:{
            type: Object,
            required: true
        }
    },
    methods:{
        toggleDonity: function(){
            this.todo.done=this.todo.done^1
            const baseURI='/item/'+String(this.todo.id)+'/done';
            this.$axios.put(baseURI,{
                done:this.todo.done
            }).then(function(response){

            }).catch(function(error){

            })
        },
        deleteTodo: function(){
            var currentID=this.todo.id;
            var point=this;
            const baseURI='/item/'+String(currentID);
            this.$axios.delete(baseURI)
            .then(function(response){
                point.$emit('todoDeleted',currentID);
            }).catch(function(error){
                
            })
        },
        updateTodo: function(changedTodo){
            this.todo=changedTodo;
        }
    }
}
</script>


