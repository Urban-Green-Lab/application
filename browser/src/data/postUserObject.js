import axios from 'axios';

const postUserInfo = (object) => new Promise((resolve, reject) => {
  axios.post('./fixtures/leaderboardData.json', object)
    .then((response) => resolve(response.data))
    .catch((error) => reject(error));
});

export default postUserInfo;
