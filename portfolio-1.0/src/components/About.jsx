import React from 'react'

import aboutImg from '../assets/about.jpg'

function About() {
  return (
    <div className='text-white max-w-[1200px] mx-auto my-12' id='about'>
        <div className="md:grid md:grid-cols-2 sm:py-16">

            <div className="mt-4 md:mt-0 text-left flex">
                <div className="my-auto mx-6">
                    <h2 className="text-4xl font-bold mb-4 primary-color">
                        About Me
                    </h2>
                    <p className="text-base lg:text-lg">
                        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Numquam ea ex, quasi fuga laborum qui, asperiores, distinctio nostrum provident hic assumenda repellat illum?
                    </p>
                </div>
            </div>

            <img className='mx-auto rounded-3xl py-8 md:py-0' src={aboutImg} width={300} height={300} alt=''/>

        </div>
    </div>
  )
}

export default About