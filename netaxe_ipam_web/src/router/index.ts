import { mapTwoLevelRouter } from '@/utils'
import { createRouter, createWebHashHistory } from 'vue-router'

const Layout = () => import('@/components/Layout.vue')

export const constantRoutes = [
  {
    path: '/login',
    name: 'Login',
    hidden: true,
    component: () => import('@/views/login/index.vue'),
  },
  {
    path: '/',
    redirect: '/index/home',
    hidden: true,
  },
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    meta: {
      noShowTabbar: true,
    },
    children: [
      {
        path: '/redirect/:path(.*)*',
        component: (): any => import('@/views/redirect/index.vue'),
      },
    ],
  },
  {
    path: '/personal',
    name: 'personal',
    component: Layout,
    hidden: true,
    meta: {
      title: '个人中心',
    },
    children: [
      {
        path: '',
        component: () => import('@/views/personal/index.vue'),
        meta: {
          title: '个人中心',
        },
      },
    ],
  },
  {
    path: '/index',
    component: Layout,
    name: 'Index',
    meta: {
      title: 'Dashboard',
      iconPrefix: 'iconfont',
      icon: 'dashboard',
    },
    children: [
      {
        path: 'home',
        name: 'Home',
        component: (): any => import('@/views/ip_manage/ipam.vue'),
        meta: {
          title: '地址管理',
          affix: true,
          cacheable: true,
          iconPrefix: 'iconfont',
          icon: 'menu',
        },
      },
      {
        path: 'task_list',
        name: 'task_list',
        component: (): any => import('@/views/task_center/task_list.vue'),
        meta: {
          title: '任务列表',
          affix: true,
          cacheable: true,
          iconPrefix: 'iconfont',
          icon: 'menu',
        },
      },
      // {
      //   path: 'net_flow',
      //   name: 'net_flow',
      //   component: (): any => import('@/views/index/net_flow.vue'),
      //   meta: {
      //     title: '网络流量',
      //     affix: false,
      //     cacheable: false,
      //     iconPrefix: 'iconfont',
      //     icon: 'menu',
      //   },
      // },
      // {
      //   hidden: true,
      //   path: 'webssh' ,
      //   name: 'webssh',
      //   component: (): any => import('@/views/index/webssh.vue'),
      //   meta: {
      //     title: 'webssh',
      //     affix: true,
      //     cacheable: true,
      //     iconPrefix: 'iconfont',
      //     icon: 'menu',
      //   },
      // },
      // {
      //   path: 'work-place',
      //   name: 'WorkPlace',
      //   component: (): any => import('@/views/index/work-place.vue'),
      //   meta: {
      //     title: '工作台',
      //     iconPrefix: 'iconfont',
      //     icon: 'menu',
      //   },
      // },
      // {
      //   path: 'dutylist',
      //   name: 'DutyList',
      //   component: (): any => import('@/views/index/dutylist.vue'),
      //   meta: {
      //     title: '值班表',
      //     iconPrefix: 'iconfont',
      //     icon: 'menu',
      //   },
      // },
    ],
  },
  // {
  //   path: '/xunmi_system',
  //   component: Layout,
  //   name: 'xunmi_system',
  //   meta: {
  //     title: '寻觅系统',
  //     iconPrefix: 'iconfont',
  //     icon: 'search',
  //   },
  //   children: [
  //     {
  //       hidden: true,
  //       path: '/address_xunmi',
  //       component: (): any => import('@/views/xunmi_system/address_xunmi.vue'),
  //       meta:{
  //         title:"寻觅系统"
  //       }
  //     }
  //   ]
  // },
  {
    path: '/404',
    name: '404',
    hidden: true,
    component: () => import('@/views/exception/404.vue'),
  },
  {
    path: '/500',
    name: '500',
    hidden: true,
    component: () => import('@/views/exception/500.vue'),
  },
  {
    path: '/403',
    name: '403',
    hidden: true,
    component: () => import('@/views/exception/403.vue'),
  },
]
const router = createRouter({
  history: createWebHashHistory(),
  routes: mapTwoLevelRouter(constantRoutes),
})

export default router
