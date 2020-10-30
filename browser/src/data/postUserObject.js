import axios from 'axios';

// FIXME: For local data
// const postUserInfo = (object) => new Promise((resolve, reject) => {
//   axios.post('./fixtures/leaderboardData.json', object)
//     .then((response) => resolve(response.data))
//     .catch((error) => reject(error));
// });

const postUserInfo = (object) => new Promise((resolve, reject) => {
  axios.post('https://sustaingame-admin.herokuapp.com/quiz_taker/', object)
    .then((response) => resolve(response.data))
    .catch((error) => reject(error));
});

export default postUserInfo;
