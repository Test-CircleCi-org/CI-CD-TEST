import user from "../../support/commands.js";

beforeEach(() => {
    cy.on('uncaught:exception', (err) => {
      if(err.message.includes('is not a function') || err.message.includes('is not defined') || err.message.includes('reading \'addEventListener\'') || err.message.includes('null (reading \'style\')'))
      {
        return false
      }
    })
    cy.visit(Cypress.env('baseUrl'))

  })
  
  describe('all projects test', () => {
    beforeEach(function() {
      cy.fixture("datareports").then(function(data) {
        this.data = data
    cy.get('#login').click()
      .loginCampusUser(user)  // Campus User is logged in before the test begins
      })
    })
     
    // 
    it('Test all projects page navigation bar', function(){
        const unoLogo = `img[alt="UNO Logo"]`,
          navigationList = '#navigationList',
          userInfo = '#accountinfo',
          projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
          .get(unoLogo).should('be.visible')
          .get(navigationList).should('be.visible').contains('Maps')
          .get(navigationList).contains('Analytics')
          .get(navigationList).contains('Projects')
          .get(navigationList).contains('Partners')
          .get(navigationList).contains('Resources')
          .get(userInfo).should('be.visible') 
      })

      it('Test all projects page navigation bar, title and footer', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          footerId = '#footer'
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
          .url().should('be.equal', Cypress.env('baseUrl')+'allProjects/')
          .get('h4').contains("All Projects").should("be.visible")
          .get(footerId).should('exist')
      })

      it('Test all projects page filter card', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filtersForm = '#filters-form'
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
          .get(filtersForm).should('be.visible')
          .get('label').contains('Academic Years')
          .get('label').contains('Project Focus Areas')
          .get('label').contains('Community Organization Types')
          .get('label').contains('College and Main Units')
          .get('label').contains('Campus Partners')
          .get('label').contains('CEC Building Partners')
          .get('label').contains('Engagement Types')
          .get('label').contains('K-12 Involvement')  
      })

      it('Test all projects page excel, pdf, hide filters and reset filters button', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filtersForm = '#filters-form',
          hideFiltersButton = `input[value="Hide Filters"]`,
          resetFiltersButton = `input[value="Reset Filters"]`
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
          .get(filtersForm).should('be.visible')
          .get('button').contains('Excel').should('be.visible').click()
          .get('button').contains('PDF').should('be.visible').click() 
          .get(hideFiltersButton).should('be.visible').click()
          .get(resetFiltersButton).should('be.visible').click()
      })

      it('Test all projects page show entries and pagination buttons functionality', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          showEntriesSelect = `select[name="example_length"]`
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
          .get(showEntriesSelect).select('10').should('exist')
          .get(showEntriesSelect).select('25').should('exist')
          .get(showEntriesSelect).select('50').should('exist')
          .get(showEntriesSelect).select('100').should('exist') 
          .get('a').contains('Previous').should('be.visible')
          .get('a').contains('1').should('be.visible').click()
          .get('a').contains('Next').should('be.visible')
      })

      it('Test projects page filter selections for academic years', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filterOptionSelection = `span[class="select2-selection select2-selection--single"]`,
          tableData = `td[class="sorting_1"]`,
          applyFiltersButtonId = '#btnApply'
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
         // selecting filter option from  academic years filters 
          .get(filterOptionSelection).contains('Previous Academic Year').click()  
          .get('#select2-id_academic_year-results').then(($li) => {
             cy.wrap($li)
               .contains(this.data.academic_year1)
               .click()
             })
               .get(applyFiltersButtonId).click()
             cy.get(tableData).contains(this.data.academic_year1)
      })

      it('Test projects page filter selections for project focus areas', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filterOptionSelection = `span[class="select2-selection__placeholder"]`,
          tableData = `td[class="sorting_1"]`  
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
         // selecting filter option from all project focus areas filters 
        .get(filterOptionSelection).contains('All Project Focus Areas').click()  
          .get('#select2-id_mission-results').then(($li) => {
             cy.wrap($li)
               .contains(this.data.focus_area2)
               .click()
             })
        cy.get('td').contains(this.data.focus_area2)
      })

      it('Test projects page filter selections for project community organization types', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filterOptionSelection = `span[class="select2-selection__placeholder"]`  
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
         // selecting filter option from all community organization types
          .get(filterOptionSelection).contains('All Community Organization Types').click()  
          .get('#select2-id_community_type-results').then(($li) => {
             cy.wrap($li)
               .contains(this.data.community_type1)
               .click()
             })
      })

      it('Test projects page filter selections for college and main units', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filterOptionSelection = `span[class="select2-selection__placeholder"]`    
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
         // selecting filter option from college and main units
          .get(filterOptionSelection).contains('All College and Main Units').click()  
          .get('#select2-id_college_name-results').then(($li) => {
             cy.wrap($li)
               .contains(this.data.college_name1)
               .click()
             })
      })
      
      it('Test projects page filter selections for campus partners', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filterOptionSelection = `span[class="select2-selection__placeholder"]`    
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
         // selecting filter option from campus partners
          .get(filterOptionSelection).contains('All Campus Partners').click()  
          .get('#select2-id_campus_partner-results').then(($li) => {
             cy.wrap($li)
               .contains(this.data.campus_partner3)
               .click()
             })
             cy.get('td').contains(this.data.campus_partner3)
      })

      it('Test projects page filter selections for CEC building partners', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filterOptionSelection = `span[class="select2-selection__placeholder"]`    
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
         // selecting filter option from CEC building partners
          .get(filterOptionSelection).contains('All (CEC/Non-CEC Partners)').click()  
          .get('#select2-id_weitz_cec_part-results').then(($li) => {
             cy.wrap($li)
               .contains(this.data.cec_part2)
               .click()
             })
      })

      it('Test projects page filter selections for Engagement types', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filterOptionSelection = `span[class="select2-selection__placeholder"]`    
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
         // selecting filter option from all engagement types
          .get(filterOptionSelection).contains('All Engagement Types').click()  
          .get('#select2-id_engagement_type-results').then(($li) => {
             cy.wrap($li)
               .contains(this.data.engagement_type2)
               .click()
             })
      })

      it('Test projects page filter selections for K-12 involvement', function(){
        const projectsId = '#projectsnav',
          allProjectsHref = `a[href="/allProjects/"]`,
          filterOptionSelection = `span[class="select2-selection__placeholder"]`    
        cy.get(projectsId).should('exist').click()
          .get(allProjectsHref).should('exist').click()
         // selecting filter option from K-12 involvement
          .get(filterOptionSelection).contains('All K-12 Involvement').click()  
          .get('#select2-id_k12_flag-results').then(($li) => {
             cy.wrap($li)
               .contains(this.data.k12_involve1)
               .click()
             })
      })
    });
  