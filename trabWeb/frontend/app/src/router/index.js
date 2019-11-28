import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/components/Index'
import Login from '@/views/Login'
import Logout from '@/views/Logout'
import ListPets from '@/components/Pets/List'
import EditPet from'@/components/Pets/Edit'
import ListVaccines from '@/components/Vaccines/List'
import Experiments from '@/components/Experiments'

Vue.use(Router)

export default new Router({
  mode: 'history',
  hash: false,
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout
    },
    {
      path: '/pets',
      name: 'ListPets',
      component: ListPets
    },
    {
      path: '/pets/edit/:id',
      name: 'EditPet',
      component: EditPet
    },
    {
    path: '/vaccines',
    name: 'ListVaccine',
    component: ListVaccines
    },
    {
      path: '/experiments',
      name: 'Experiments',
      component: Experiments
    }
  ]
})
