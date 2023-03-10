import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { FavoritesComponent } from './favorites/favorites.component';
import { RouterModule } from '@angular/router';
import { MyAccountComponent } from './my-account/my-account.component';
import { HomeComponent } from './home/home.component';
import { CommonModule } from '@angular/common';
import { LayoutModule } from '@angular/cdk/layout';
import { MaterialModule } from './material-module';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CarouselModule } from 'ngx-owl-carousel-o';
import { FlexLayoutModule } from '@angular/flex-layout';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SingleGameComponent } from './single-game/single-game.component';
import { StarRatingModule } from 'angular-star-rating';
import { SearchComponent } from './search/search.component';
import { NgToastModule, NgToastService } from 'ng-angular-popup';
import { DialogComponent } from './dialog/dialog.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { HtmlEntitiesPipe } from './pipe/html-entities.pipe';
import { RecommendationsComponent } from './recommendations/recommendations.component';
import { HttpClientXsrfModule } from '@angular/common/http';
import { CookieModule } from 'ngx-cookie';
import { HttpRequestInterceptor } from './interceptors/HttpRequestInterceptor';


@NgModule({
  declarations: [
    AppComponent,
    FavoritesComponent,
    MyAccountComponent,
    HomeComponent,
    LoginComponent,
    RegisterComponent,
    SingleGameComponent,
    SearchComponent,
    DialogComponent,
    PageNotFoundComponent,
    HtmlEntitiesPipe,
    RecommendationsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule,
    CommonModule,
    LayoutModule,
    MaterialModule,
    BrowserAnimationsModule,
    CarouselModule,
    FlexLayoutModule,
    FormsModule,
    ReactiveFormsModule,
    StarRatingModule.forRoot(),
    NgToastModule,
    HttpClientXsrfModule.withOptions({
      headerName: 'X-CSRFToken'
    }),
    CookieModule.withOptions()
  ],
  providers: [[{ provide: HTTP_INTERCEPTORS, useClass: HttpRequestInterceptor, multi: true }]],
  bootstrap: [AppComponent],
  entryComponents: [DialogComponent]
})
export class AppModule { }
