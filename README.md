const profile = {
  name: 'Fredrick Onyango',
  title: 'Full-Stack Developer | Cloud Enthusiast|Backend lover | Problem Solver',CineCreatives,
  Skills: [
  'React', 'NextJS', 'Python', 'Express',
  'MySQL', 'MongoDB', 'Docker', 'AWS', 
  'RESTAPIs', 'Git', 'Linux', 'Nginx',
  'TypeScript', 'Node.js', 'GraphQL', 'Redis',
  'Kubernetes', 'CI/CD', 'Jenkins', 'Terraform',
  'Postman', 'Swagger', 'Microservices', 'Webpack',
  'HTML', 'CSS', 'Sass', 'TailwindCSS', 'Bootstrap',
  'Serverless','Prometheus', 'Grafana'
],

  hardWorker: true,
  quickLearner: true,
  problemSolver: true,
  yearsOfExperience: 5,
  hireable: function () {
    return (
      this.hardWorker &&
      this.problemSolver &&
      this.skills.length >= 6 &&
      this.yearsOfExperience >= 4
    );
  }
};
