import { BrowserModule } from '@angular/platform-browser';
import { NgModule, APP_INITIALIZER } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {
    MdSortModule, MdTableModule, MdDatepickerModule, MdInputModule, MdCardModule, MdCheckboxModule, MdButtonModule,
    MdDialogModule, MdSelectModule, MdNativeDateModule
} from '@angular/material';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import 'hammerjs';
import { Ng2CompleterModule } from 'ng2-completer';
import { AccordionModule } from 'primeng/components/accordion/accordion';
import {CalendarModule, SharedModule, ChartModule} from 'primeng/primeng';
import { AppRoutingModule } from './app-routing.module';
import { MdIconModule } from '@angular/material';

// Components
import { AppComponent } from './app.component';
import { HomepageComponent } from './components/homepage/homepage.component';

// Services
import { CookieService } from 'ngx-cookie-service';


// Functions
import { FilterPipe } from './filter.pipe';


@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    BsDropdownModule.forRoot(),
    FormsModule,
    HttpModule,
    MdInputModule,
    MdCardModule,
    MdCheckboxModule,
    MdButtonModule,
    MdSelectModule,
    BsDropdownModule.forRoot(),
    Ng2CompleterModule,
    MdDialogModule,
    MdSelectModule,
    Ng2CompleterModule,
    AccordionModule,
    SharedModule,
    MdIconModule,
    MdDatepickerModule,
    MdNativeDateModule,
    CalendarModule,
    SharedModule,
    ChartModule,
    MdTableModule,
    MdSortModule,
    AppRoutingModule // Add routes to the app
  ],
  entryComponents: [
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
