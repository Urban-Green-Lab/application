import axios from 'axios';

// FIXME: For local data
// const getLeaderBoardInfo = () => new Promise((resolve, reject) => {
//   axios.get('./fixtures/leaderboardData.json')
//     .then((response) => resolve(response.data))
//     .catch((error) => reject(error));
// });

const getLeaderBoardInfo = () => new Promise((resolve, reject) => {
  axios.get('https://sustaingame-admin.herokuapp.com/leaderboard/')
    .then((response) => resolve(response.data))
    .catch((error) => reject(error));
});

export default getLeaderBoardInfo;
