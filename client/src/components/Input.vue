<template>

<div class="collapse" v-bind:id="'input-content-'+todo.id">
    <div>
        <div class="d-flex justify-content-center">
            <div class="d-flex flex-column">
                <div class="p-2">
                    제목
                    <input type="text" class="form-control" id="subject" v-model="subject">
                </div>
                <div class="p-2">
                    내용
                    <textarea class="form-control" rows="5" id="content" v-model="content"></textarea>
                </div>
                <div class="p-2">
                    우선순위
                    <select class="custom-select-sm p-2" v-model="priority">
                    <option selected>우선순위</option>
                    <option value="1">1</option>                           
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                </div>
                <div class="p-2"></div>
                <div class="p-2">
                    <label for="expiration">기한</label>
                    <input class="form-control" type="datetime-local" v-model="expiration"/>
                </div>
                <div class="p-2">
                    <div class="row">
                            <div class="col">
                                <button class="btn btn-secondary" @click="updateTodo" data-toggle="collapse" v-bind:data-target="'#input-content-'+todo.id">저장</button>
                            </div>
                            <div class="col">
                                <button class="btn btn-warning" data-toggle="collapse" v-bind:data-target="'#input-content-'+todo.id" >취소</button>
                            </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="row">
                
            </div>
        </div>
    </div>
</div>
                    
</template>

<script>
export default {
    name: 'Todo',
    props:{
        todo:{
            type: Object,
            required: true
        }
    },
    data() {
        return {
            id:this.todo.id,
            subject:this.todo.subject,
            content:this.todo.content,
            priority:this.todo.priority,
            expiration:this.todo.expiration,
            done:this.todo.done
        }
    },
    methods:{
        updateTodo: function(){
            var changedTodo=new Object();
            changedTodo.id=this.id;
            changedTodo.subject=this.subject;
            changedTodo.content=this.content;
            changedTodo.priority=this.priority;
            changedTodo.expiration=this.expiration;
            changedTodo.done=this.done;
            this.$emit('todoChanged',changedTodo);
            const baseURI='/item/'+String(this.todo.id);
            this.$axios.put(baseURI,{
                id:this.id,
                subject:this.subject,
                content:this.content,
                priority:this.priority,
                expiration:this.expiration
            }).then(function(response){
                
            }).catch(function(error){
                
            })
        },
    }
}
</script>


