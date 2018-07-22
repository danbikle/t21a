Rails.application.routes.draw do
  get 'home/index'
  get 'home/about'
  get 'home/contact'
  get 'home/blog'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root 'home#index'
  get  '/about',   to: 'home#about'
  get  '/blog',    to: 'home#blog'
  get  '/contact', to: 'home#contact'
  get ':controller(/:action)'  
end
