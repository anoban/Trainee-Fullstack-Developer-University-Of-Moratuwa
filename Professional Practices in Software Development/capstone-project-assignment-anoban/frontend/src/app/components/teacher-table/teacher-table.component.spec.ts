import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TeacherTableComponent } from './teacher-table.component';

describe('TeacherTableComponent', () => {
  let component: TeacherTableComponent;
  let fixture: ComponentFixture<TeacherTableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TeacherTableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TeacherTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
