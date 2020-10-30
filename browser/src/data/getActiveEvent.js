import axios from 'axios';

const getActiveEvent = () => new Promise((resolve, reject) => {
  axios.get('/fixtures/activeEventQuizzesData.json')
    .then((response) => resolve(response.data))
    .catch((error) => reject(error));
});

export default getActiveEvent;
