// Page [ trello/trello_vue/src/stores/user.js ]
import { defineStore } from 'pinia'
import axios from 'axios'
export const useUserStore = defineStore({
    id: 'user',
    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            name: null,
            surname: null,
            email: null,
            date_of_birth: null,
            access: null,
            refresh: null,
            friends_count: 0,
            // User gender 👤
            gender: null,
            // 🖼️ Profile picture
            // 🖼 صورة الملف الشخصي
            avatar: null,
            // 🖼️ Cover photo
            // 🖼️ صورة الغلاف
            cover: null,
            // 📋 Number of tasks
            // 📋 عدد المهام
            task_count: 0
        }
    }),
    actions: {
        // 🔄 Initialize the store
        // 🔄 تهيئة المخزن
        initStore() {
            if (localStorage.getItem('user.access')) {
                console.log('User has access!')
                this.user.isAuthenticated = true
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.surname = localStorage.getItem('user.surname')
                this.user.email = localStorage.getItem('user.email')
                this.user.date_of_birth = localStorage.getItem('user.date_of_birth')
                this.user.gender = localStorage.getItem('user.gender')
                this.user.avatar = localStorage.getItem('user.avatar')
                this.user.cover = localStorage.getItem('user.cover')
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.refreshToken()
                this.user.friends_count = localStorage.getItem('user.friends_count')
                this.user.task_count = localStorage.getItem('user.task_count')

            }
        },
        // 🔑 Set access and refresh tokens
        // 🔑 إعداد رموز الوصول والتحديث
        setToken(data) {
            console.log('setToken', data)
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },
        // ❌ Remove tokens and clear user data
        // ❌ إزالة الرموز ومسح بيانات المستخدم
        removeToken() {
            console.log('removeToken')
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.name = null
            this.user.surname = null
            this.user.email = null
            this.user.date_of_birth = null
            this.user.gender = null
            this.user.avatar = null
            this.user.cover = null
            this.user.friends_count = null
            this.user.task_count = null

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.surname', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.date_of_birth', '')
            localStorage.setItem('user.gender', '')
            localStorage.setItem('user.avatar', '')
            localStorage.setItem('user.cover', '')
            localStorage.setItem('user.friends_count', '')
            localStorage.setItem('user.task_count', '')
        },
        // ✍️ Set user info in state and localStorage
        // ✍️ تعيين بيانات المستخدم في الحالة و localStorage
        setUserInfo(user) {
            console.log('setUserInfo', user)
            this.user.id = user.id
            this.user.name = user.name
            this.user.surname = user.surname
            this.user.email = user.email
            this.user.date_of_birth = user.date_of_birth
            this.user.gender = user.gender
            this.user.avatar = user.avatar
            this.user.cover = user.cover
            this.user.friends_count = user.friends_count
            this.user.task_count = user.task_count
            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.surname', this.user.surname)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.date_of_birth', this.user.date_of_birth)
            localStorage.setItem('user.gender', this.user.gender)
            localStorage.setItem('user.avatar', this.user.avatar)
            localStorage.setItem('user.cover', this.user.cover)
            localStorage.setItem('user.friends_count', this.user.friends_count)
            localStorage.setItem('user.task_count', this.user.task_count)
        },
        // 🔄 Refresh access token
        // 🔄 تحديث رمز الوصول
        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access
                    localStorage.setItem('user.access', response.data.access)
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)
                    this.removeToken()
                })
        },
    }
})
