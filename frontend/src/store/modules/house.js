import house from '../../api/house'

const state = {
  list: [],
  detail: {},
  suggestion: [{name: "Loading", id: "Loading", price:"Loading", suggested_reason:["Loading","Loading"]}],
  roommates: [],
}

const getters = {}

const actions = {
  getList ({ commit }, query) {
    house.getHouseList(houses => {
      commit('setHouseList', houses)
    }, query)
  },
  deleteHouseObj ({ commit }, id) {
    house.deleteHouse(id, houses => {
      commit('setHouseList', houses)
    })
  },
  createHouseObj ({ commit }, data) {
    house.createHouse(data, houses => {
      commit('setHouseList', houses)
    })
  },

  editHouseObj ({ commit }, payload) {
    house.editHouse(payload.data, payload.id, houses => {
      commit('setHouseDetail', houses)
    })
  },

  getHouseDetailObj({ commit }, id) {
    house.getHouseDetail(id, house => {
      commit('setHouseDetail', house)
    })
  },

  likeHouseList({ commit }, data) {
    house.likeHouse(data, houses => {
      // commit('setHouseList', houses)
    })
  },
  likeHouseObj({ commit }, data) {
    house.likeHouseDetail(data, houses => {
      commit('setHouseDetail', houses)
    })
  },
  getSuggestions({ commit }) {
    house.getSuggestionHouse(houses => {
      commit('setSuggestions', houses)
    })
  },
  getRoommates({ commit }) {
    house.getRoommate(roommates => {
      commit('setRoommates', roommates)
    })
  },
}


const mutations = {
  setHouseList(state, houses) {
    state.list = houses
  },
  setHouseDetail(state, house) {
    state.detail = house
  },
  setSuggestions(state, houses) {
    state.suggestion = houses
  },
  setRoommates(state, rm) {
    state.roommates = rm
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
