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
                                <div class="dropdown-header">우선순위</div>
                                <a href="#" class="dropdown-item">올림</a>
                                <a href="#" class="dropdown-item">내림</a>
                                <div class="dropdown-divider"></div>
                                <a href="#" class="dropdown-item"><div class="text-warning">삭제</div></a>
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
</li>
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
    methods:{
        toggleDonity: function(){
            this.todo.done=this.todo.done^1
        }
    }
}
</script>


