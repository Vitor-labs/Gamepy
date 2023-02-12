import React from "react";
import Header from "./../components/header";
import Banner from "./../components/banner";
import Carousel from "./../components/carousel";
import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <>
      <Header />
      <br />
      <Banner />
      <Carousel />
      <div className="container mx-auto p-6">
        <p className="text-center text-3xl font-semibold tracking-wide">Welcome to our shop</p>
        <p className="text-center py-4">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in
          commodo sapien, vitae rhoncus ipsum. Integer euismod, quam a
          ullamcorper congue, eros nibh vestibulum dolor, sit amet congue nisl
          erat eu libero.
        </p>
        <Link to="/products">
          <button className="mx-auto text-center py-3 px-5 rounded-md bg-violet-400 text-white font-semibold tracking-wide">
            Shop now
          </button>
        </Link>
      </div>
    </>
  );
};

export default HomePage;
