import React from "react";
import "../Styles/home.css";

export const Home = () => {
    return (
        <div>
            <div className="container content">
                <div className="row">
                    <div className="col-sm-3 talk">
                        <h1>FJob</h1>
                        <h2>Find job quicker</h2>
                        <br />
                        <h6 className="bold-four">
                            FJob collects data on job offers from many websites to help you find the best offer easily and quickly.
                    </h6>
                        <br />
                        <h6><a className="btn btn-dark start start-two" href="/offers">Get Started</a></h6>
                    </div>
                    <div className="col-sm-9 showcase-img">
                        <img src="../../../public/images/reading-woman.png " alt="Reading Woman" className="img-fluid" />
                    </div>
                </div>
            </div>

            <section className="features-icons bg-light text-center det-ails">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-4">
                            <div className="features-icons-item mx-auto mb-5 mb-lg-0 mb-lg-3">
                                <div className="features-icons-icon d-flex  icon-bra-ails">
                                    <i className="icon-screen-desktop m-auto text-primary icon-ails"></i>
                                </div>
                                <h5>Job offer scrapers</h5>
                                <p className="lead mb-0">Every day many scrapers collects and process data from many websites!</p>
                            </div>
                        </div>
                        <div className="col-lg-4">
                            <div className="features-icons-item mx-auto mb-5 mb-lg-0 mb-lg-3">
                                <div className="features-icons-icon d-flex  icon-bra-ails">
                                    <i className="icon-layers m-auto text-primary icon-ails"></i>
                                </div>
                                <h5>Offers from companies</h5>
                                <p className="lead mb-0">Companies can post job offers here for free!</p>
                            </div>
                        </div>
                        <div className="col-lg-4">
                            <div className="features-icons-item mx-auto mb-0 mb-lg-3">
                                <div className="features-icons-icon d-flex  icon-bra-ails">
                                    <i className="icon-check m-auto text-primary icon-ails"></i>
                                </div>
                                <h5>Notifications</h5>
                                <p className="lead mb-0">Sign up to get emails about new job offers every day!</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
}