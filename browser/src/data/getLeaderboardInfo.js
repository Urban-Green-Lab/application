import axios from 'axios';

const getLeaderBoardInfo = () => new Promise((resolve, reject) => {
  axios.get('./fixtures/leaderboardData.json')
    .then((response) => resolve(response.data))
    .catch((error) => reject(error));
});

export default getLeaderBoardInfo;
