# Personality Recommender for Twitter - Backend
Recommends Twitter posts based on user's personality.

## Authors
Yaoxian Qu <quyaoxian@gmail.com> and Xuanrui Qi <me@xuanruiqi.com>.

## License
MIT License. See "LICENSE" file for details.

Backend for personality recommender app. Calculates user personality with watson personality insights API and determines recommendations with k-means clustering. Run locally on port 5000.

About personality recommender:

Personality recommender is an app that pulls tweets of the logged in user from twitter, calculate his/her personality with watson personality insights API, and recommend other users with similar personality to the user based on k-means clustering algorithm.
The app utilizes angular.js for frontend and flask for backend with firebase as database.


