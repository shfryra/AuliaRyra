/* General Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
    color: #333;
  }
  header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
  }
  header nav ul {
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin: 0;
  }
  header nav ul li {
    margin: 0 15px;
  }
  header nav ul li a {
    color: #fff;
    text-decoration: none;
    font-size: 1.2rem;
  }
  
  /* Hero Section */
  #hero {
    background: url('hero.jpg') no-repeat center center/cover;
    color: #fff;
    text-align: center;
    padding: 100px 20px;
  }
  #hero h1 {
    font-size: 3rem;
  }
  #hero p {
    font-size: 1.2rem;
  }
  #hero .btn {
    display: inline-block;
    margin-top: 20px;
    padding: 10px 20px;
    background: #fff;
    color: #333;
    text-decoration: none;
    font-weight: bold;
  }
  
  /* Section Styles */
  section {
    padding: 50px 20px;
    text-align: center;
  }
  .projects {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
  }
  .project img {
    width: 100%;
    height: auto;
    border-radius: 5px;
  }
  
  /* Footer */
  footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 20px 0;
  }